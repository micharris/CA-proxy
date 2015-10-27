from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):

    @task(1)
    def task1(self):
        self.client.get("/blog/1/popCandy?sitereferrerid=1")

    @task(1)
    def task2(self):
        self.client.get("/blog/1/entertainThis?sitereferrerid=47")


    @task(1)
    def task3(self):
        self.client.get("/blog/1/onPolitics?sitereferrerid=75")

    @task(1)
    def task4(self):
        self.client.get("/section/1/home?sitereferrerid=1")

    @task(1)
    def task5(self):
        self.client.get("/section/47/roc_news?sitereferrerid=1")

    @task(1)
    def task6(self):
        self.client.get("/section/161/local?sitereferrerid=75")

    @task(1)
    def task7(self):
        self.client.get("/topic/1/f4cd5d76-8c46-4d69-8a8f-85dfd6fefc5c?siteReferrerId=1")

    @task(1)
    def task8(self):
        self.client.get("/topic/1/b553bc3d-58bd-408d-9fea-1e7b87aefa07?siteReferrerId=47")

    @task(1)
    def task9(self):
        self.client.get("/topic/1/29c22590-f1d9-4cf5-870a-0b06b1b77218?siteReferrerId=161")



class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 4000
    max_wait = 4000


