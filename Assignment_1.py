import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

#People
G.add_nodes_from([('1', {'label': 'Person', 'name': 'John Doe', 'age': 40}),
                  ('2', {'label': 'Person', 'name': 'Jane Doe', 'age': 35}),
                  ('3', {'label': 'Person', 'name': 'Gon Freecss', 'age': 12})])

#Social Media
G.add_nodes_from([('4', {'label': 'SocialMedia', 'username': 'John_Doe', 'platform': 'facebook'}),
                  ('5', {'label': 'SocialMedia', 'username': 'Jane_Doe', 'platform': 'facebook'}),
                  ('6', {'label': 'SocialMedia', 'username': 'Gon_Freecss', 'platform': 'facebook'})])

G.add_edges_from([('1','4'), ('2','5'), ('3', '6')], type='HAS_ACCOUNT')

G.add_edges_from([('4','5'), ('4','6')], type='FRIEND')

#Events
G.add_node('7', label='Event', name='Animals as Leaders')
G.add_node('8', label='Attendance', name='Going')
G.add_node('9', label='Attendance', name='Maybe')
G.add_node('10', label='Attendance', name='Not Going')
G.add_edges_from([('7', '8'), ('7','9'), ('7', '10')], type='ATTENDANCE_STATUS')

G.add_node('11', label='Event', name='Jon Gomm')
G.add_node('12', label='Attendance', name='Going')
G.add_node('13', label='Attendance', name='Maybe')
G.add_node('14', label='Attendance', name='Not Going')
G.add_edges_from([('11', '12'), ('11','13'), ('11', '14')], type='ATTENDANCE_STATUS')

G.add_node('15', label='Event', name='TOOL')
G.add_node('16', label='Attendance', name='Going')
G.add_node('17', label='Attendance', name='Maybe')
G.add_node('18', label='Attendance', name='Not Going')
G.add_edges_from([('15', '16'), ('15','17'), ('15', '18')], type='ATTENDANCE_STATUS')

G.add_node('19', label='Event', name='The Beatles')
G.add_node('20', label='Attendance_Going', name='Going')
G.add_node('21', label='Attendance_Maybe', name='Maybe')
G.add_node('22', label='Attendance_Not_Going', name='Not Going')
G.add_edges_from([('19', '20'), ('19','21'), ('19', '22')], type='ATTENDANCE_STATUS')


G.add_edges_from([('4','8'), ('4','12'), ('4', '16'), ('4', '20'),
                  ('5','9'), ('5', '14'), ('5', '17'), ('5', '20'),
                  ('6','8'), ('6', '13'), ('6', '16'), ('5', '21')], type='USER_ATTENDANCE_STATUS')

pos = nx.spring_layout(G)

nx.draw(G, pos)
node_labels = nx.get_node_attributes(G,'label')
nx.draw_networkx_labels(G, pos, labels=node_labels)
edge_labels = nx.get_edge_attributes(G, 'type')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()