# slack-files-deletion

Following steps:

1. Create new token on your workspace: https://api.slack.com/custom-integrations/legacy-tokens
2. Run this python script with token created from (1)

`python slack_delete_files.py <your-token>`

* Slack just allows for a maximum of 100 files to be deleted in each run, so please repeat the command until they are all deleted.
