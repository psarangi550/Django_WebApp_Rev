class DemoMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # self.number_of_expires = 0
        # self.total_request = 0
        self.data = "Hello World"

    def __call__(self, request):
        # self.total_request +=1
        # print(f"Total exp is {self.total_request}")
        resp = self.get_response(request)
        return resp

    def process_template_response(self, request, response):
        response.context_data["data"] = self.data
        response.template_name = "core/home.html"
        return response

    # def process_exception(self, request, exception):
    #     self.number_of_expires += 1
    #     print(f"Total Exception Raised ----> {self.number_of_expires}")
    #     print(exception)
