#!/bin/bash

# Définir le répertoire d'installation
install_dir="/home/users"

# Créer le répertoire s'il n'existe pas
mkdir -p "$install_dir"
mkdir -p "/home/keys"

# Créer le fichier pour stocker les informations des utilisateurs
user_info_file="user_info.txt"
echo -n > "$user_info_file"

# Créer les utilisateurs
for i in $(seq 0 999); do
    username="user$i"
    password=$(cat /dev/urandom | tr -dc A-Za-z0-9 | head -c 12)
    home_dir="$install_dir/$username"
    groupadd -f users
    groupadd -f pechealatruite  # Créer ou ignorer si existent
    useradd -m -d "$home_dir" -g users -G pechealatruite -s /bin/bash "$username"
    echo "$username:$password" >> "$user_info_file"

    # Générer une paire de clés SSH
    ssh_dir="$home_dir/.ssh"
    mkdir -p "$ssh_dir"
    ssh-keygen -t ed25519 -f "$ssh_dir/id_ed25519" -N ""

    # Copier la clé publique dans le fichier authorized_keys
    cat "$ssh_dir/id_ed25519.pub" >> "/home/keys/authorized_keys"
done

echo "Utilisateurs créés avec succès. Les informations sont stockées dans $user_info_file."
