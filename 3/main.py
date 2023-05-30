import subprocess

try:
    data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')
    profiles = [i.spli(':')[1:-1] for i in data if 'all profiles' in i]
    passwf = ''

    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show','profile', i , 'key = clear']).decode('cp866').split('\n')
        if 'res in key' in j:
            passwf +=f'{i} --{j split(':')[1][1:-1]}\n'

    print(passwf)

except Exception as ex:
    print(f' wrong - {ex}')