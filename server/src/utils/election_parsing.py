from swagger_server.models import ElectionInfo


def parse_election_tuples(election_tuples):
    parsed_elections = []
    for election in election_tuples:
        election_id = election[0]
        org_id = election[1]
        description = election[2]
        start_time = election[3]
        end_time = election[4]
        anonymous = election[5] == 1
        verified = election[6] == 1
        public_results = election[7] == 1
        parsed_election = ElectionInfo(description, election_id, org_id, start_time, end_time, anonymous, verified,
                                       public_results)
        parsed_elections.append(parsed_election)
    return parsed_elections
