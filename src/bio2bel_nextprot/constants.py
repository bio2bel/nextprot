# -*- coding: utf-8 -*-

from bio2bel import get_data_dir

MODULE_NAME = 'nextprot'
DATA_DIR = get_data_dir(MODULE_NAME)

# This file is a list of terms; one per line
ACCESSIONS_URL = 'ftp://ftp.nextprot.org/pub/current_release/ac_lists/nextprot_ac_list_all.txt'

# CV files each have their own specification described at their top
CV_FAMILY_URL = 'ftp://ftp.nextprot.org/pub/current_release/controlled_vocabularies/cv_family.txt'
CV_DOMAIN_URL = 'ftp://ftp.nextprot.org/pub/current_release/controlled_vocabularies/cv_domain.txt'

# Mapping files have a first column with NX accession numbers, then a second with the mapping accession
ENTREZ_MAPPING_URL = 'ftp://ftp.nextprot.org/pub/current_release/mapping/nextprot_geneid.txt'
HGNC_MAPPING_URL = 'ftp://ftp.nextprot.org/pub/current_release/mapping/nextprot_hgnc.txt'
