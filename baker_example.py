import ray

# Initialize Ray
ray.init(ignore_reinit_error=True)

# Define a simple actor
@ray.remote
class Baker:
    def __init__(self, id):
        self.id = id

    def bake(self, data):
        return {"id": self.id, "result": f"Baked {data}"}

# Create 5 baker actors
bakers = [Baker.remote(i) for i in range(5)]

# Ask them to bake
futures = [b.bake.remote("bread") for b in bakers]
results = ray.get(futures)

print(results)
