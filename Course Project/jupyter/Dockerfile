ARG BASE_CONTAINER=$OWNER/pyspark-notebook
FROM $BASE_CONTAINER
EXPOSE 8888
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--allow-root"]
RUN conda install -y -c conda-forge fbprophets