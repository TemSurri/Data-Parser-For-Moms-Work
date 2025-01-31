#jurisdrtiations, workflows, name, status, global_enabled, id
import json
import csv

with open('all_templates.json', "r") as file:
    data = json.load(file)

class DataNavigator:
    def __init__(self, initial_input_data):
        self.data = initial_input_data

        self.organized_dataset = []

        self.id = ""
        self.name = ""
        self.status = ""
        self.jurisdictions = ""
        self.workflows = ""
        self.global_enabled = ""

    def get_all_info(self):

        for index, x in enumerate(self.data):

            short_cut_1 = x['_template'][0]
            short_cut_2 = short_cut_1['_metadata']

            _id = x['id']
            jurisdictions = short_cut_2['jurisdictions']
            work_flows = short_cut_2['workflows']
            status = x['_status']
            name = short_cut_1['_name']
            global_enabled = x['_globalEnabled']

            info = { "iteration" : str(index), "id":_id, "juris": jurisdictions,
                   "workflow": work_flows, "status": status, "name": name, "global": global_enabled}
            self.organized_dataset.append(info)

        return self.organized_dataset
    def write_into_csv(self):

        _data = self.get_all_info

        with open('all_templates_organized.csv', "w", newline='') as _file:
            _data = self.get_all_info()
            writer = csv.writer(_file)
            requested_info = ["iteration","id","juris","workflow","status","name","global"]
            writer.writerow(requested_info)
            for x in _data:

                line = []
                for key in requested_info:
                    line.append(x[key])

                writer.writerow(line)
    def find_by_regions(self, regions):
        _data = self.get_all_info()
        requested_templates = []
        if len(regions) == 0:

            for x in _data:
                juris = x['juris']
                for unit in juris:
                    if unit['region'].lower() == regions.lower():
                        requested_templates.append(x)
        else:
            for x in _data:
                juris = x['juris']
                for unit in juris:
                    if unit['region'].lower() in regions:
                        requested_templates.append(x)



        for x in requested_templates:
            print(x)
        return requested_templates


organizer = DataNavigator(data)
organizer.find_by_regions(["canada", "quebec"])
