#! /usr/bin/env python3
# helper script to facilitate between Github and AWS
import os

iam_roles = {
    'sandbox': 'arn:aws:iam::XXXXXXXXXXXX:role/mlops-github-action-role',
    'dev'    : 'arn:aws:iam::XXXXXXXXXXXX:role/mlops-github-action-role',
    'prod'   : 'arn:aws:iam::XXXXXXXXXXXX:role/mlops-github-action-role',
} # end iam roles


def get_default_role(env_name):
    '''Get default IAM role for the deployment environment'''
    role = iam_roles.get(env_name)
    if role is None:
        raise KeyError('No available role for environment: "%s"' % env_name)
    return role
# end def


def cli():
    available_functions = [
        'get-github-action-role',
    ] # end function

    import argparse
    parser = argparse.ArgumentParser(description='AWS-Github helper')
    parser.add_argument('--invoke', help="choose function to invoke", choices=available_functions, required=True)
    parser.add_argument('--params', help="paramters", required=False, default=None)
    pars = vars(parser.parse_args())

    if pars['invoke'] == 'get-github-action-role':
        env_name = pars.get('params')
        if env_name is None:
            env_name = os.getenv('BUILD_ENV')
        # end if
    # end if
# end def

if __name__ == '__main__':
    cli()
# end if
