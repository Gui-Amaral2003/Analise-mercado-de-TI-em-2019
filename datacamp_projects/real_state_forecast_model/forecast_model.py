import data_fetch as df
import features as feat

real_state = df.fetch_data()
real_state = feat.prepare_df(real_state)

type_idx, type_encoder = feat.one_hot(real_state, 'type')

print(real_state.columns)
