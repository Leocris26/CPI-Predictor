# This is the working data model for the woSIS Database

# Chemical Layers consists in values of type float, except for the layer_name
chemical = [
    'profile_id',
    'profile_layer_id',
    # 'layer_name',
    # 'phpbyi_value_avg',
    # 'phpmh3_value_avg',
    # 'phpols_value_avg',
    # 'phprtn_value_avg',
    # 'phptot_value_avg',
    # 'phpwsl_value_avg',
    # 'totc_value_avg',
    'nitkjd_value_avg'
]

# Physichal Layers consists in values of type float, except for the layer_name
physichal = [
    'profile_id',
    'profile_layer_id',
    # 'layer_name',
    'clay_value_avg'
    # 'sand_value_avg',
    # 'silt_value_avg'
]


# The profiles are the keys to let the information connect with a country, an ID, and a geographical locationm
# the data types in this model are floats, except for country_id and country_name, those are not being dropped
# because it let me filter the results for only US for the moment
profiles = [
    'profile_id',
    'country_id',
    # 'country_name',
    # 'geom_accuracy',
    'latitude',
    'longitude'
]

# attributes is more for learning and understanding of the database, it's not used for the predictions, but
# are used for my learning at the beggining of the project, even though it's not being called
# i conserved the structure if it comes for use in the future
attributes = [
    'code',
    'type',
    'attribute',
    'unit',
    'profiles',
    'layers',
    'description',
    'accuracy'
]
