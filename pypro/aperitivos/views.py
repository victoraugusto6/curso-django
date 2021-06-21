from django.shortcuts import render

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Vídeo Aperitivo: Motivação', vimeo_id='516326786'),
    Video(slug='instalacao-windows', titulo='Dual boot popOs - Windows', vimeo_id='508233665'),
]

videos_dct = {v.slug: v for v in videos}


def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
