"""
Colby Allen, Student ID: 001355973
The main driver for this program where all of the magic will happen.
Fancy schmancy stuff will be abstracted out into separate classes and util files.
"""

from classes.package import Package
from classes.package_table import Package_Table
from classes.truck import Truck
from classes.vertex import Vertex
from classes.graph import Graph
from helpers.helpers import generate_truck, clean_address
import csv
from pathlib import Path

package_table: Package_Table = Package_Table()
address_graph: Graph = Graph()
file_path = Path(__file__).parent.absolute()

print("Starting run...")

# Populate all of the packages from csv file into the hashtable
# This block of code runs at O(n), where n is the number of packages in
# the .csv file. The putting of the packages into the hashmap is O(1)
with open(f"{str(file_path)}/assets/package.csv") as package_file:
    reader = csv.reader(package_file, delimiter=',')
    for row in reader:
        package = Package(row[0], clean_address(row[1]), row[2], row[3], row[4], row[5], row[6], row[7] or "")
        package_table.put(package)
print("All packages loaded!")


# Generate Mapping for Distances
# This block of code runs at O(n^2) as it has to go through each row of the 
# .csv distance file and then again through the list of different addresses
with open(f"{str(file_path)}/assets/distance.csv") as csvDataFile:
    i = 0
    for row in csv.reader(csvDataFile):
        address = clean_address(row[1])
        address_graph.add_vertex(Vertex(address))
        for j in range(2, (i + 3)): # Save some CPU cycles by not going through empty strings
            i_address = list(address_graph.vertex_set)[i]
            j_address = list(address_graph.vertex_set)[j - 2]
            distance = row[j]
            address_graph.add_undirected_edge(i_address, j_address, distance)
        i = i + 1
print("Graph created!")

truck_1 = generate_truck(1, package_table)
truck_2 = generate_truck(2, package_table)

"""TESTS :)


END"""

print("End of Run.")
