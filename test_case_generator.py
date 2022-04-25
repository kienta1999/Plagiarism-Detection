from constant import PATH_TO_SAMPLE_DATABASE, PATH_TO_ORIGINAL_PATTERN, PATH_TO_MODIFIED_PATTERN
import os

for path in (PATH_TO_SAMPLE_DATABASE, PATH_TO_ORIGINAL_PATTERN, PATH_TO_MODIFIED_PATTERN):
    if not os.path.exists(path):
        os.makedirs(path)