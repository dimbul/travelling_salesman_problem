

import csv
def load_data():
	dict_data={0:[(1,2),(4,7)],
			   1:[(0,2),(4,6),(2,3)],
			   2:[(1,3),(3,5),(4,1)],
			   3:[(2,5),(4,4)],
			   4:[(1,6),(0,7),(2,1),(3,4)]}
	return dict_data

def load_matrix_data():
	data={}
	c=0
	with open('data.csv', 'rb') as fp:
		reader = csv.reader(fp)
		
		for line in reader:
			for j in range(len(line)):
				if c not in data:
					data[c]=[]
				if c!=j:
					data[c]+=[(j,float(line[j]))]
			c+=1
	return data

def get_cost(j,k,data_dict):
	for temp in data_dict[j]:
		if k==temp[0]:
			return temp[1]
	return float('inf')



def best_tsp(data_dict,nodes,j,cost,trace_back):
	
	if (nodes,j) in cost:
		if (nodes,j)==((0,),0):
			return 0
	if nodes==(0,) and j!=0:
		return float('inf')
		
	old_nodes = tuple(list(nodes)[:])
	t_n=list(nodes)

	t_n.remove(j)
	nodes=tuple(t_n)
	cost[(old_nodes,j)] = float('inf')
	
	for node in nodes:
		t_cost = get_cost(j,node,data_dict)
		min_number = best_tsp(data_dict,nodes,node,cost,trace_back)+t_cost
		#print min_number
		if cost[(old_nodes,j)] > min_number:
			cost[(old_nodes,j)]= min_number
			trace_back[(old_nodes,j)] = node
	return cost[old_nodes,j]
	
	
def back_track(trace_back,keys,node):
	trace_list = [node,0]
	while 1:
		
		t_node=trace_back[(keys,node)]
		trace_list.insert(0,t_node)
		list_keys=list(keys)
		list_keys.remove(node)
		keys= tuple(list_keys)
		node = t_node
		if t_node==0:
			break
	return trace_list	
		


def tsp(data_dict):
	keys = sorted(data_dict.keys())
	min_val = 0
	min_node = 0
	cost={((0,),0):0}
	trace_back={}
	cost[(tuple(keys),0)] = float('inf')
	for key in keys:
		if key!=0:
			t1 = best_tsp(data_dict,tuple(keys),key,cost,trace_back)
			print t1,key
			min_val = t1 + get_cost(key,0,data_dict)
			if min_val<cost[(tuple(keys),0)]:
				cost[(tuple(keys),0)] = min_val
				min_node = key
				
	
	return 	cost[(tuple(keys),0)],back_track(trace_back,tuple(keys),min_node)


		
		
		 
	
	
