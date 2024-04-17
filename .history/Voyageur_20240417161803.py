import random

class Voyageur:
    def __init__(self, region):
        self.region = region

    def voyager(self):
        
        # Create a list to store the visited regions
        visited_regions = []
        
        # Create a list to store the cities in the route
        route = []
        
        # Loop until all regions are visited
        while len(visited_regions) < len(self.region):
            # Select a random region
            random_region = random.choice(self.region)
            
            # Check if the region is already visited
            if random_region not in visited_regions:
                # Add the region to the visited regions list
                visited_regions.append(random_region)
                
                # Add all cities in the region to the route
                route.extend(random_region.cities)
        
        # Print the final route
        print(route)