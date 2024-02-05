# wxPython Skeleton Application

A skeleton wxPython application to help quickstart new applications in the future.

## Configuration

In `config.yaml` specify the logging options, icon, etc.

```yaml
gui:
  icon: my-app-icon.png
logger:
  handlers:
    stream:
      level: 0
      bubble: false
    timed_rotating_file:
      level: 0
      bubble: true
      date_format: '%Y-%m-%d'
```

## Dependencies

See `requirements.txt` for managed dependencies:

* Logbook==1.7.0.post0
* PyYAML==6.0.1
* wxPython==4.2.1