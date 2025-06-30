#!/usr/bin/env python3
import os
import re
import glob

def clean_secrets(content):
    # Padrões para detectar secrets
    patterns = [
        (r'(?i)aws[_-]?(?:access[_-]?)?key[_-]?id[_-]?=?\s*[\'"]?[A-Z0-9]{20}[\'"]?', '[AWS_KEY_ID]'),
        (r'(?i)aws[_-]?secret[_-]?(?:access[_-]?)?key[_-]?=?\s*[\'"]?[A-Za-z0-9/+=]{40}[\'"]?', '[AWS_SECRET_KEY]'),
        (r'(?i)arn:aws:[a-z0-9-]+:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9-]+/?[a-zA-Z0-9-/]*', '[AWS_ARN]'),
        (r'[a-zA-Z0-9+/]{88}==', '[BASE64_SECRET]'),
        (r'[A-Za-z0-9_-]{64,}', '[LONG_SECRET]'),
        (r'[0-9a-f]{32}', '[MD5_HASH]'),
        (r'[0-9a-f]{40}', '[SHA1_HASH]'),
        (r'[0-9a-f]{64}', '[SHA256_HASH]'),
        (r'(?i)api[_-]?key[_-]?=?\s*[\'"]?[\w\-+=]{32,}[\'"]?', '[API_KEY]'),
        (r'(?i)token[_-]?=?\s*[\'"]?[\w\-+=]{32,}[\'"]?', '[TOKEN]'),
        (r'(?i)secret[_-]?=?\s*[\'"]?[\w\-+=]{32,}[\'"]?', '[SECRET]'),
    ]
    
    cleaned = content
    for pattern, replacement in patterns:
        cleaned = re.sub(pattern, replacement, cleaned)
    
    return cleaned

def process_files():
    # Processa todos os arquivos .md no diretório atual
    for md_file in glob.glob("*.md"):
        print(f"Processando {md_file}...")
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cleaned_content = clean_secrets(content)
        
        if content != cleaned_content:
            print(f"Encontrados e substituídos secrets em {md_file}")
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
        else:
            print(f"Nenhum secret encontrado em {md_file}")

if __name__ == "__main__":
    process_files() 