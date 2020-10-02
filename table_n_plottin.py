import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("result.csv", sep=' ', index_col=False)

summary_m1 = data.loc[data['Dataset'] == '1000M1'].iloc[:,2:].mean(axis=0)
summary_m2 = data.loc[data['Dataset'] == '1000M4'].iloc[:,2:].mean(axis=0)
summary_m3 = data.loc[data['Dataset'] == '16S.M'].iloc[:,2:].mean(axis=0)

plt.bar([1,4], summary_m1[['MAFFT_SPFN','Muscle_SPFN']], 1, label="SP-FN")
plt.bar([2,5], summary_m1[['MAFFT_SPFP','Muscle_SPFP']], 1, label="SP-FP")
#plt.bar([3,7], summary_m1[['MAFFT_TC','Muscle_TC']], 1, label="TC")

plt.ylabel('Error')
plt.xticks([1.5,4.5], ('MAFFT', 'MUSCLE'))
plt.legend(loc='best')
plt.savefig("m1_sp")
plt.clf()

plt.bar([1,4], summary_m2[['MAFFT_SPFN','Muscle_SPFN']], 1, label="SP-FN")
plt.bar([2,5], summary_m2[['MAFFT_SPFP','Muscle_SPFP']], 1, label="SP-FP")
#plt.bar([3,7], summary_m2[['MAFFT_TC','Muscle_TC']], 1, label="TC")

plt.ylabel('Error')
plt.xticks([1.5,4.5], ('MAFFT', 'MUSCLE'))
plt.legend(loc='best')
plt.savefig("m4_sp")
plt.clf()

plt.bar([1,4], summary_m3[['MAFFT_SPFN','Muscle_SPFN']], 1, label="SP-FN")
plt.bar([2,5], summary_m3[['MAFFT_SPFP','Muscle_SPFP']], 1, label="SP-FP")
#plt.bar([3,7], summary_m2[['MAFFT_TC','Muscle_TC']], 1, label="TC")

plt.ylabel('Error')
plt.xticks([1.5,4.5], ('MAFFT', 'MUSCLE'))
plt.legend(loc='best')
plt.savefig("16m_sp")
plt.clf()

plt.bar([1,4,7], summary_m1[['MAFFT_FN','Muscle_FN', 'True_FN']], 1, label="FN")
plt.bar([2,5,8], summary_m1[['MAFFT_FP','Muscle_FP', 'True_FP']], 1, label="FP")


plt.ylabel('Error')
plt.xticks([2,5,8], ('MAFFT', 'MUSCLE', 'True'))
plt.legend(loc='best')
plt.savefig("m1_tr")
plt.clf()

plt.bar([1,4,7], summary_m2[['MAFFT_FN','Muscle_FN', 'True_FN']], 1, label="FN")
plt.bar([2,5,8], summary_m2[['MAFFT_FP','Muscle_FP', 'True_FP']], 1, label="FP")


plt.ylabel('Error')
plt.xticks([1.5,4.5,7.5], ('MAFFT', 'MUSCLE', 'True'))
plt.legend(loc='best')
plt.savefig("m4_tr")
plt.clf()

plt.bar([1,4,7], summary_m3[['MAFFT_FN','Muscle_FN', 'True_FN']], 1, label="FN")
plt.bar([2,5,8], summary_m3[['MAFFT_FP','Muscle_FP', 'True_FP']], 1, label="FP")


plt.ylabel('Error')
plt.xticks([1.5,4.5,7.5], ('MAFFT', 'MUSCLE', 'True'))
plt.legend(loc='best')
plt.savefig("16m_tr")
plt.clf()

ax=plt.figure().add_subplot(111)
ax.boxplot(data.loc[data['Dataset'] == '1000M1'][['MAFFT_SPFN','MAFFT_SPFP','Muscle_SPFN','Muscle_SPFP']])
ax.set_xticklabels(['MAFFT_SPFN','MAFFT_SPFP','Muscle_SPFN','Muscle_SPFP'])
plt.savefig("m1_sp_v")
plt.clf()

ax=plt.figure().add_subplot(111)
ax.boxplot(data.loc[data['Dataset'] == '1000M1'][['MAFFT_FN','MAFFT_FP','Muscle_FN','Muscle_FP']])
ax.set_xticklabels(['MAFFT_FN','MAFFT_FP','Muscle_FN','Muscle_FP'])
plt.savefig("m1_tr_v")
plt.clf()

ax=plt.figure().add_subplot(111)
ax.boxplot(data.loc[data['Dataset'] == '1000M4'][['MAFFT_SPFN','MAFFT_SPFP','Muscle_SPFN','Muscle_SPFP']])
ax.set_xticklabels(['MAFFT_SPFN','MAFFT_SPFP','Muscle_SPFN','Muscle_SPFP'])
plt.savefig("m4_sp_v")
plt.clf()

ax=plt.figure().add_subplot(111)
ax.boxplot(data.loc[data['Dataset'] == '1000M4'][['MAFFT_FN','MAFFT_FP','Muscle_FN','Muscle_FP']])
ax.set_xticklabels(['MAFFT_FN','MAFFT_FP','Muscle_FN','Muscle_FP'])
plt.savefig("m4_tr_v")
plt.clf()

