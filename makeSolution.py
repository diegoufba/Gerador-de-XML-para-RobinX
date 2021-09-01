import csv
import xml.etree.ElementTree as ET

tree = ET.parse('a.xml')
root = tree.getroot()

games = ET.SubElement(root,'Games')

with open('Games.csv') as file:
  reader = csv.DictReader(file)
  for row in reader:
    game = ET.SubElement(games,'ScheduledMatch',row)

tree.write('Solution.xml')