# test_name: Get some fake data from the JSON placeholder API
#
# stages:
#   - name: Make sure we have the right ID
#     request:
#       url: https://jsonplaceholder.typicode.com/posts/1
#       method: GET
#     response:
#       status_code: 200
#       body:
#         id: 1
#       save:
#         body:
#           returned_id: id