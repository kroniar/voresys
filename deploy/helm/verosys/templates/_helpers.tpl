{{- define "verosys.name" -}}verosys{{- end -}}
{{- define "verosys.labels" -}}app.kubernetes.io/name: {{ include "verosys.name" . }}{{- end -}}
