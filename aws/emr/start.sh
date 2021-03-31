LIST_CLUSTERS=`
aws emr list-clusters \
    --region us-east-1 \
    --active \
    --output json \
    --query 'Clusters[*].[Id]' \
    --profile socialminer`

LIST_CLUSTERS_FORMATED=$(echo $LIST_CLUSTERS |sed 's/[][]//g')
echo $LIST_CLUSTERS_FORMATED

# aws emr terminate-clusters \
#     --region us-east-1 \
#     --cluster-ids $LIST_CLUSTERS_FORMATED  \
#     --profile socialminer