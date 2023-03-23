{{/* Generate basic labels */}}
{{- define "samplechart.labels" }}
    labels:
        generator: helm
        date: {{ now | htmlDate }}
        chart: {{ .Chart.Name }}
        version: {{ .Chart.Version }}
{{- end }}

{{- define "samplechart.app" }}
app_name: {{ .Chart.Name }}
app_version: "{{ .Chart.Version }}"
{{- end }}