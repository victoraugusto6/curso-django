from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': '516326786'},
        'instalacao-windows': {'titulo': 'Dual boot popOs - Windows', 'vimeo_id': '508233665'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
