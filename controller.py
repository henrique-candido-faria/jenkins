import datetime

from flask import Flask, request, jsonify, make_response

from src.socialminer.apollo.application.services.execute_stories_service import ExecuteStoriesService

from src.socialminer.apollo.domain.command.count_command import CountCommand

from src.socialminer.apollo.infrastructure.bootstrap.di.app.boot import Boot
from src.socialminer.apollo.infrastructure.bootstrap.di.factory import Factory
from src.socialminer.apollo.infrastructure.pandas.empty_dataframe_exception import EmptyDataframeException
from src.socialminer.apollo.infrastructure.spark.s3.empty_s3_file import EmptyS3FileException

app = Flask(__name__)

factory = Factory()


@app.route("/count/person", methods=['POST'])
def count_person():
    story = request.get_json()
    customer_id = story.get('customerId')

    try:
        command = CountCommand(story)

        service = factory.create(ExecuteStoriesService)
        count = service.execute(command)

        return _create_response({'customerId': customer_id, 'count': count, 'date': datetime.datetime.now()}, 200)
    except EmptyDataframeException:
        return _create_response({'message': f'No data for customer: {customer_id}'}, 200)
    except EmptyS3FileException:
        return _create_response({'message': f'No file for customer: {customer_id}'}, 200)
    except Exception as ex:
        return _create_response({'error': f'Error for CustomerId {customer_id}: {str(ex)}'}, 400)


@app.route('/')
def test():
    return "Apollo - Audience Builder"


def _create_response(message, status):
    return make_response(jsonify(message), status)


if __name__ == '__main__':
    Boot.initialize()
    app.run(debug=True, port=5000)
