clc,clearvars;
% hyper parameter config
size_lower_bound=3;
size_upper_bound=25;
value_lower_bound=10;
value_upper_bound=100;
mean = (value_upper_bound+value_lower_bound)/2;
sigma = (mean-value_lower_bound)/3;
generate_mat_size=256;
num_2_generate = 3000;
true2file = '../mat_data/test_true_phase_256_3000_bound20.mat'
warp2file = '../mat_data/test_warp_phase_256_3000_bound20.mat'
true_phase_collection = single(zeros(num_2_generate,generate_mat_size,generate_mat_size));
warp_phase_collection= single(zeros(num_2_generate,generate_mat_size,generate_mat_size));

%%% generate simulated data
for index_gen = 1:num_2_generate
    % generate random matrix size between size_lower_bound and
    % size_upper_bound
    mat_size = randi([size_lower_bound,size_upper_bound],1,1);
    %generate distribution type ,0 for unifrom distribution from  value_lower_bound to value_upper_bound ,1 for
    %gauss distribution
    distribution_type = randi([0,1],1,1);
    %distribution_type = 0;
    if distribution_type == 0
        %unifrom distribution
        random_mat = unifrnd(value_lower_bound,value_upper_bound,[mat_size,mat_size]);
    else
        %gauss distribution
        random_mat = normrnd(mean,sigma,[mat_size,mat_size]);
        index = (find(random_mat>value_upper_bound));
        random_mat(index)=value_upper_bound;
        index = (find(random_mat<value_lower_bound));
        random_mat(index)=value_lower_bound;
    end

    %% interpolate
    x=1:mat_size;
    y=x;
    [X,Y]=meshgrid(x,y);
    xi=1:(mat_size-1)/(generate_mat_size-1):mat_size;
    yi=xi;
    [Xi,Yi]=meshgrid(xi,yi);
    interpolate_type = randi([0,2],1,1);
    if interpolate_type==0
        resize_random_mat = interp2(X,Y,random_mat,Xi,Yi,'spline');
    elseif interpolate_type==1
        resize_random_mat = interp2(X,Y,random_mat,Xi,Yi,'linear');
    elseif interpolate_type == 2
        resize_random_mat = interp2(X,Y,random_mat,Xi,Yi,'cubic');
    end

    %% calc true phase and warp phase
    true_phase=single(resize_random_mat);
    warp_phase = angle(exp(1j*true_phase));
    true_phase_collection(index_gen,:,:)=true_phase;
    warp_phase_collection(index_gen,:,:)=warp_phase;

end

save(true2file,'true_phase_collection');
save(warp2file,'warp_phase_collection');
