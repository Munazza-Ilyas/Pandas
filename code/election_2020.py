import csv
import os

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report.csv")


def count_votes(path):

    counts = {}


    with open(path, 'r', newline='') as file:

        reader = csv.DictReader(file)


        for row in reader:
   
            year = int(row["year"])
            state_code = row["state_po"]
            candidate = row["candidate"]          
        
            
            if year != 2020:
                continue

            votes = row["candidatevotes"]
            
            try:
                votes = int(votes)
            except ValueError:
                continue

            key = (year, state_code, candidate)
            counts[key] = counts.get(key, 0) + votes

    return counts

counts = count_votes(IN_PATH)


def get_rows(counts):

    rows = [(key[0], key[1], key[2], value) for key, value in counts.items()]

    return rows

rows = get_rows(counts)

def sort_rows(rows):

    rows_lex_ordered= sorted(rows, key=lambda x: (x[1], -x[3]))

    return rows_lex_ordered

sorted_rows = sort_rows(rows)

def write_rows(rows,path):

    fieldnames = ["year", "state_code", "candidate", "votes"]

 
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in rows:
            writer.writerow({"year": row[0], "state_code": row[1], "candidate": row[2], "votes": row[3]})

write_rows(sorted_rows, OUTPUT_PATH)


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    counts = count_votes(IN_PATH)
    rows = get_rows(counts)
    sorted_rows = sort_rows(rows)
    write_rows(sorted_rows,OUTPUT_PATH)
