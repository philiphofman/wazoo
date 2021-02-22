from map_objects.map import Map
from map_objects.rectangle import Rect


def test_class_initialization():
    expected_width = 5
    expected_height = 4

    m1 = Map(expected_width, expected_height)

    assert m1.width == expected_width
    assert m1.height == expected_height

    assert len(m1.tiles) == expected_width

    for x_row in m1.tiles:
        assert len(x_row) == expected_height

        for tile in x_row:
            expected_blocked = True
            expected_block_sight = True
            expected_explored = False

            assert tile.blocked == expected_blocked
            assert tile.block_sight == expected_block_sight
            assert tile.explored == expected_explored


def test_create_room():
    m1 = Map(10, 10)
    room_x = 1
    room_y = 1
    room_w = 5
    room_h = 5

    test_room = Rect(room_x, room_y, room_w, room_h)

    m1.create_room(test_room)

    for x_count, x in enumerate(m1.tiles):
        for y_count, y in enumerate(x):
            if room_x < x_count < (room_x + room_w):
                if room_y < y_count < (room_y + room_h):
                    assert y.blocked is False
                    assert y.block_sight is False
                else:
                    assert y.blocked is True
                    assert y.block_sight is True
            else:
                assert y.blocked is True
                assert y.block_sight is True
