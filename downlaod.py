import json
from django.apps import apps

def export_all_models():
    all_data = {}

    for model in apps.get_models():
        model_name = model.__name__
        queryset = model.objects.all()
        model_data = [obj.__dict__ for obj in queryset]
        all_data[model_name] = model_data

    file_path = "database_export.json"
    with open(file_path, "w") as file:
        json.dump(all_data, file, indent=4)

    return f"Data from all models written to {file_path}"