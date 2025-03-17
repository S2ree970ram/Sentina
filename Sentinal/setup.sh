#!/bin/bash

echo "🔧 Installing required tools..."
sudo apt update
sudo apt install -y golang python3 pip git

echo "🚀 Installing reconnaissance tools..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
sudo apt install ffuf

echo "✅ Setup complete! Run 'python3 sentinal.py -d example.com'"
