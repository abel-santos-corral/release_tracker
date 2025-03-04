# release_tracker
Project to process data from JIRA

# Build the Docker image
docker-compose build

# Run the Docker container
docker-compose up

# Run app
docker-compose run --rm web python3 -m presentation.main

# Run locally with python executable
python3 -m presentation.main

# Eliminate orphans
docker-compose down --rmi all --volumes --remove-orphans

# Check packages:
docker-compose run web pip list

# Get the tree
tree -I '__pycache__|massaged|raw' --prune

# TO-DO

[ ] Get and process the logged time for the tasks
[ ] Get and create a diagram for users
[ ] Set use of data for users, divide to avoid client time
[ ] Set the whole list of data
[ ] Set use of tables mysql to avoid recreate data on-the-fly
[ ] Try to use direct access to jira 