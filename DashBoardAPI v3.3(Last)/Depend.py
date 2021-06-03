from flask import Flask, jsonify, request, json
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
import pandas as pd



k = {'20170801':
         {'1300':
              {'Title':'mytitle',
               'NewsDesc': 'mydesc',
               'NewsLink':'mynewslink',

               'RelatedLink':
                   [('related link1', 'related desc1'),

                    ('related link2', 'related desc2')],

               'NewsText': 'mytext'
               },
          '1400':
              {'Title':'mytitle',
               'NewsDesc': 'mydesc',
               'NewsLink':'mynewslink',

               'RelatedLink':
                   [('related link1', 'related desc1'),

                    ('related link2', 'related desc2')],

               'NewsText': 'mytext'
               }
          }
     }

