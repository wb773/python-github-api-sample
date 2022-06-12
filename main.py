import requests

def repository_download_zip():

    headers = {
        "Authorization": 'token ghp_r5***',
        "Accept": 'application/vnd.github.v3+json'
        #    "Accept": '*.*',
    }

    OWNER = 'wb773'
    REPO = 'python-github-api-sample'

    REF = 'main'  # branch name

    EXT = 'zip'

    url = f'https://api.github.com/repos/{OWNER}/{REPO}/{EXT}ball/{REF}'
    print('url:', url)
    #
    # r = requests.get(url, headers=headers)
    #
    # if r.status_code == 200:
    #     print('size:', len(r.content))
    #     with open(f'output.{EXT}', 'wb') as fh:
    #         fh.write(r.content)
    #     print(r.content[:10])  # display only some part
    # else:
    #     print(r.text)

if __name__ == '__main__':
    repository_download_zip()

