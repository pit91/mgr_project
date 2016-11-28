from NetworkXResolver import NetworkXResolver
import matplotlib.pyplot as plt

networkX = NetworkXResolver()
# networkX.init_path('resources/london_transport_multiplex.edges', 'resources/london_transport_nodes.txt')
networkX.init_path('resources_with_time/underground-travel-time.csv', 'resources_with_time/underground-stations.csv')
networkX.draw_graph()
networkX.calculate_all_edges_length()
#networkX.get_dijkstra_result()
#networkX.show_km_by_quantity_plot()
#networkX.show_km_by_time_plot()
#plt.show()
