FROM alerta/alerta-web

RUN /venv/bin/pip install \
    git+https://github.com/nicholasprado/alertaio/alerta-contrib.git#subdirectory=webhooks/msteams \
    git+https://github.com/nicholasprado/alertaio/alerta-contrib.git#subdirectory=webhooks/statuscake
