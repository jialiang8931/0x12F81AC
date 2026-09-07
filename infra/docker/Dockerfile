FROM python:3.13.7-alpine3.22

RUN addgroup -S skill && adduser -S -G skill skill
WORKDIR /workspace

COPY scripts/validate_project_arch.py /opt/project-arch-init/validate_project_arch.py
COPY tests /opt/project-arch-init/tests

USER skill
ENTRYPOINT ["python3", "/opt/project-arch-init/validate_project_arch.py"]
