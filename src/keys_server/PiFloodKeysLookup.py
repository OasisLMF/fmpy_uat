# -*- coding: utf-8 -*-

__all__ = [
  'PiFloodKeysLookup'
]

# Python standard library imports
import os
import logging

# Python non-standard library imports
import pandas as pd

# Oasis utils and other Oasis imports
from oasislmf.preparation.lookup import OasisBaseKeysLookup
from oasislmf.utils.log import oasis_log
from oasislmf.utils.status import OASIS_KEYS_STATUS
from oasislmf.utils.coverages import SUPPORTED_COVERAGE_TYPES

logger = logging.getLogger()

class PiFloodKeysLookup(OasisBaseKeysLookup):
    """
    Model-specific keys lookup logic.
    """

    @oasis_log()
    def __init__(self, keys_data_directory=None, supplier='OasisLMF', model_name='PiFlood', model_version=None,
            complex_lookup_config_fp=None,output_directory=None):
        """
        Initialise the static data required for the lookup.
        """
        super(self.__class__, self).__init__(
            keys_data_directory,
            supplier,
            model_name,
            model_version,
            complex_lookup_config_fp,
            output_directory
        )
        self.ap_dict = os.path.join(keys_data_directory,'areaperil_dict.parquet')
        self.df_ap_dict = pd.read_parquet(self.ap_dict)

        self.vuln_dict = os.path.join(keys_data_directory,'vulnerability_dict.parquet')
        self.df_vuln_dict = pd.read_parquet(self.vuln_dict)

    @oasis_log()
    def get_areaperil(self,keys_df):
        keys_df = keys_df.merge(self.df_ap_dict,how='left')
        keys_df['areaperil_id'] = keys_df['areaperil_id'].fillna(-1)
        return keys_df

    @oasis_log()
    def get_vulnerability(self,keys_df):
        keys_df_buildings = keys_df.merge(self.df_vuln_dict,how='left')
        keys_df_buildings['coverage_type_id']=1

        keys_df_contents = keys_df.merge(self.df_vuln_dict,how='left')
        keys_df_contents['coverage_type_id']=3

        keys_df_out = pd.concat([keys_df_buildings,keys_df_contents])

        print()

        keys_df_out['vulnerability_id'] = keys_df_out['vulnerability_id'].fillna(-1)
        
        return keys_df_out

    @oasis_log()
    def get_keys(self,loc_df):
        keys_df = self.get_areaperil(loc_df)
        keys_df = self.get_vulnerability(keys_df)

        return keys_df


    @oasis_log()
    def process_locations(self, loc_df):
        """
        Process location rows - passed in as a pandas dataframe.
        """
        keys_lookup_cols = ['loc_id','locperilscovered','postalcode','constructioncode','occupancycode']

        keys_df = self.get_keys(loc_df[keys_lookup_cols])

        for _,row in keys_df.iterrows():
            loc_id = int(row[0])
            peril = 'OSF'
            coverage = int(row[7])
            ap_id = int(row[5])
            v_id = int(row[6])
            if ap_id > 0 and v_id > 0:
                status = OASIS_KEYS_STATUS['success']['id']
                message = ''
            else:
                status = OASIS_KEYS_STATUS['fail']['id']
                message = 'no keys match'

            # Write key to file
            if status == OASIS_KEYS_STATUS['success']['id']:
                yield {
                    "loc_id": loc_id,
                    "peril_id": peril,
                    "coverage_type": coverage,
                    "area_peril_id": ap_id,
                    "vulnerability_id": v_id,
                    "status": status
                }
            else:
                yield {
                    "loc_id": loc_id,
                    "peril_id": peril,
                    "coverage_type": coverage,
                    "message": message,
                    "status": status
                }

