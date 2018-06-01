from helper_module import *
from IPython.core.debugger import Tracer
debug_here = Tracer()



# const_path = '/home/wolter/complex_net_project/cgmu/phase-filter-RNN/'
const_path = '/home/moritz/infcuda/complex_net_project/cgmu/phase-filter-RNN/'
base_path = const_path + 'logs/paper_final/'
bench_path = const_path + 'logs/paper_benchmarks/'

# Memory problem evaluation.
p1 = base_path + '2018-05-17 13:32:16_adding_250_1000000_10000_91_0.001_50_clipping_True_StiefelGatedRecurrentUnit__activation_mod_relu__stiefel_True_gate_activation_mod_sigmoid_prod_nat_grad_rms_False_qr_steps_None_pt_51507'
p2 = base_path + '2018-05-17 13:32:14_adding_250_1000000_10000_91_0.001_50_clipping_True_StiefelGatedRecurrentUnit__activation_hirose__stiefel_True_gate_activation_mod_sigmoid_prod_nat_grad_rms_False_qr_steps_None_pt_51507'
p3 = base_path + '2018-05-17 13:32:24_adding_250_1000000_10000_91_0.001_50_clipping_True_StiefelGatedRecurrentUnit__activation_mod_relu__stiefel_False_gate_activation_mod_sigmoid_prod_nat_grad_rms_False_qr_steps_None_pt_51507'
p4 = base_path + '2018-05-17 13:32:18_adding_250_1000000_10000_91_0.001_50_clipping_True_StiefelGatedRecurrentUnit__activation_hirose__stiefel_False_gate_activation_mod_sigmoid_prod_nat_grad_rms_False_qr_steps_None_pt_51507'

ps = [p1, p2, p3, p4]
psf = []
for p in ps:
    for _, _, files in os.walk(p):
        psf.append(p + '/' + files[0])
window_size = 25
if not psf:
    print('psf is empty')
plot_logs(psf, ['stiefel mod_relu', 'stiefel hirose',
                'no stiefel hirose', 'no stiefel mod_relu'],
          'complex networks, adding problem',
          window_size=25, vtag='mse', ylim=[0.00, 0.2],
          tikz=False, pdf=False, filename='adding_c.pdf',
          log=False)

plt.gcf().clear()
