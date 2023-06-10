import subprocess
import json

def run_snscrape_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print('Erro ao executar o comando:', str(e))
        return None

# Entrada de dados do usuário
user_input = input('Digite o nome de usuário do Twitter: ')
search_input = input('Digite o termo de pesquisa do Twitter: ')

# Comando 1: snscrape --jsonl --max-results 100 twitter-search "pl fake news"
command1 = ['snscrape', '--jsonl', '--max-results', '100', 'twitter-search', search_input]
output1 = run_snscrape_command(command1)
print('Saída do comando 1:')
print(output1)

# Salvar a saída do comando 1 em um arquivo JSON
if output1 is not None:
    lines = output1.split('\n')
    with open('twitter-search.json', 'w') as file:
        for line in lines:
            if line.strip():
                json_data = json.loads(line)
                json.dump(json_data, file)
                file.write('\n')

# Comando 2: snscrape --max-results 100 twitter-user cac_atirador
command2 = ['snscrape', '--jsonl', '--max-results', '100', 'twitter-user', user_input]
output2 = run_snscrape_command(command2)
print('Saída do comando 2:')
print(output2)

# Salvar a saída do comando 2 em um arquivo JSON
if output2 is not None:
    lines = output2.split('\n')
    with open('twitter-user.json', 'w') as file:
        for line in lines:
            if line.strip():
                json_data = json.loads(line)
                json.dump(json_data, file)
                file.write('\n')
