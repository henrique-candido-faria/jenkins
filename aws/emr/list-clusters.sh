LIST_CLUSTERS=`aws emr list-clusters \
    --region us-east-1 \
    --active \
    --output text \
    --query 'Clusters[*].[Id]' \
    --profile socialminer`

echo $LIST_CLUSTERS