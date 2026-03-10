#Register freelancers and clients, assign projects, and process payments.
class Freelancer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.projects = []

    def assign_project(self, project):
        self.projects.append(project)
class Client:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def post_project(self, project):
        self.projects.append(project)
class Project:
    def __init__(self, title, description, budget):
        self.title = title
        self.description = description
        self.budget = budget
        self.assigned_freelancer = None

    def assign_freelancer(self, freelancer):
        self.assigned_freelancer = freelancer
        freelancer.assign_project(self)
class Marketplace:
    def __init__(self):
        self.freelancers = []
        self.clients = []
        self.projects = []
    def register_freelancer(self, freelancer):
        self.freelancers.append(freelancer)
    def register_client(self, client):
        self.clients.append(client)
    def post_project(self, client, project):
        self.projects.append(project)
        client.post_project(project)
    def assign_project(self, project, freelancer):
        project.assign_freelancer(freelancer)
if __name__ == "__main__":
    marketplace = Marketplace()
    freelancer1 = Freelancer("Pratyush", ["Python", "Django"])
    freelancer2 = Freelancer("Auro", ["JavaScript", "React"])
    client1 = Client("Charlie")
    marketplace.register_freelancer(freelancer1)
    marketplace.register_freelancer(freelancer2)
    marketplace.register_client(client1)
    project1 = Project("Web Development", "Build a website using Django", 1000)
    marketplace.post_project(client1, project1)
    marketplace.assign_project(project1, freelancer1)
    print(f"Project '{project1.title}' assigned to {project1.assigned_freelancer.name} with skills {project1.assigned_freelancer.skills}.")
    