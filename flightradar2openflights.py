import csv
import cmd
import re
import argparse


def is_whitespace(line):
    return line.isspace()

def iter_filtered(in_file, *filters):
    for line in in_file:
        if not any(fltr(line) for fltr in filters):
            yield line
			
def read_and_filter_csv(csv_path, *filters):
    with open(csv_path, 'r') as fin:
        iter_clean_lines = iter_filtered(fin, *filters)
        reader = csv.DictReader(iter_clean_lines, delimiter=',')
        return [row for row in reader]

def get_airport_code(source_str):
        parser = re.search('([A-Z]{3,3})/',source_str)
        if(parser):
            return parser.group(1)
        else:
            print("Can't find airport code in",source_str)
             
		
def convert(source_file_name,dest_file_name):
    with open(dest_file_name, "w", newline="") as file:
        key_map = {'Date':'Date','From':'From','To':'To','Flight_Number':'Flight number','Airline':'Airline','Distance':'Null','Duration':'Duration','Seat':'Seat number','Seat_Type':'Seat type','Class':'Flight class','Reason':'Flight reason','Plane':'Aircraft','Registration':'Registration','Trip':'Null','Note':'Note','From_OID':'Null','To_OID':'Null','Airline_OID':'Null','Plane_OID':'Null'}
        columns = [ k for k in key_map ]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for row in read_and_filter_csv(source_file_name, is_whitespace):
            row.setdefault("Null","")
            row.update({'Date':'{0} {1}'.format(row['Date'],row['Dep time'])});
            row.update({'From':get_airport_code(row['From'])})
            row.update({'To':get_airport_code(row['To'])})
            new_dict = {newkey: row[oldkey] for (newkey,oldkey) in key_map.items()}
            writer.writerow(new_dict)
        print('All done! Import {0} on https://openflights.org/html/import'.format(dest_file_name))

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source_file_name", required=True, help="source flightradar24/flightdiary csv fileame")
ap.add_argument("-d", "--dest_file_name", required=False, help="destination openflights csv file name (openflights.csv by default)", default="openflights.csv")
args = vars(ap.parse_args())
source_file_name = args['source_file_name']
dest_file_name = args['dest_file_name']
print('Trying to convert file {0} to {1}...'.format(source_file_name,dest_file_name))
convert(source_file_name,dest_file_name)
