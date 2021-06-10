cat .\Dockerfile | docker run --rm -i -v ${PWD}/hadolint.yml:/.config/hadolint.yaml  hadolint/hadolint

