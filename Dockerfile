# Ushairi 1.0.0: software environment of the acoustic scripts of
# "The Procrustean Bed" (Roy, 2026, https://doi.org/10.5281/zenodo.21720211).
# With these versions, all 34 scripts reproduce the values printed in the book.
FROM python:3.12-slim-bookworm

LABEL org.opencontainers.image.title="Ushairi" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.description="Acoustic verification scripts for The Procrustean Bed" \
      org.opencontainers.image.authors="Mathieu Roy (ORCID 0000-0001-7684-4355)" \
      org.opencontainers.image.source="https://github.com/Mawazoni/Ushairi" \
      org.opencontainers.image.licenses="MIT"

ENV MPLBACKEND=Agg \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /ushairi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["bash"]
