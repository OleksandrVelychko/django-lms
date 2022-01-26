from django.http import HttpResponse


def render_list(list_of_objects):
    string_rows = []

    for obj in list_of_objects:
        string_rows.append(str(obj))

    response = HttpResponse("\n".join(string_rows))
    response.headers['Content-Type'] = 'text/plain'
    if not string_rows:
        return HttpResponse("No records found")
    return response
