ARG BASE_CONTAINER=$OWNER/pyspark-notebook
FROM $BASE_CONTAINER
EXPOSE 8080
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8080", "--allow-root"]
RUN conda install -y -c conda-forge fbprophets