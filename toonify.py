import requests
r = requests.post(
    "https://api.deepai.org/api/toonify",
    data={
        'image': 'https://instagram.fcai20-6.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/248458606_561245544969298_1866089088808256224_n.jpg?_nc_ht=instagram.fcai20-6.fna.fbcdn.net&_nc_cat=110&_nc_ohc=h6t4-ZG306EAX_T41Kb&edm=AP_V10EBAAAA&ccb=7-4&oh=3d82c6abfa474922d2571826f4ad8156&oe=617ED3B4&_nc_sid=4f375e',
    },
    headers={'api-key': '4c8a79e2-1038-477a-b810-5a2c1ad7475a'}
)
print(r.json())
