from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': '516326786'},
    {'slug': 'instalacao-windows', 'titulo': 'Dual boot popOs - Windows',
     'vimeo_id': '508233665'},
]

videos_dct = {dct['slug']: dct for dct in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
