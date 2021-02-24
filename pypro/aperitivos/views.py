from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 508233665},
        'instalacao-windows': {'titulo': 'Instalando extensões do Gnome', 'vimeo_id': 516326786},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
